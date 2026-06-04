from datetime import datetime

from app.repositories.scan_repository import (
    ScanRepository,
)

from app.repositories.ocr_result_repository import (
    OCRResultRepository,
)

from app.repositories.threat_finding_repository import (
    ThreatFindingRepository,
)

from app.services.storage_service import (
    StorageService,
)

from app.services.ocr_service import (
    OCRService,
)

from app.services.threat_detection_service import (
    ThreatDetectionService,
)

from app.services.threat_score_service import (
    ThreatScoreService,
)

from app.services.risk_level_service import (
    RiskLevelService,
)

from app.services.text_normalizer_service import (
    TextNormalizerService,
)

from app.services.url_repair_service import (
    UrlRepairService,
)

from app.services.scam_classifier_service import (
    ScamClassifierService,
)

from app.repositories.classification_repository import (
    ClassificationRepository,
)

from app.services.recommendation_service import (
    RecommendationService,
)

from app.services.brand_detection_service import (
    BrandDetectionService,
)

from app.services.context_analysis_service import (
    ContextAnalysisService,
)

from app.services.domain_intelligence_service import (
    DomainIntelligenceService,
)

from app.services.threat_intelligence_service import (
    ThreatIntelligenceService,
)

from app.services.risk_narrative_service import (
    RiskNarrativeService,
)

from app.services.domain_reputation_finding_service import (
    DomainReputationFindingService
)

from app.services.threat_explanation_service import (
    ThreatExplanationService
)

from app.services.risk_narrative_service import (
    RiskNarrativeService
)

from app.services.action_recommendation_service import (
    ActionRecommendationService
)

from app.services.ocr_quality_service import (
    OCRQualityService
)

from app.services.whois_service import (
    WhoisService
)

from app.services.domain_age_service import (
    DomainAgeService
)

from app.repositories.report_repository import (
    ReportRepository
)

from app.services.ioc_service import (
    IOCService
)

from app.services.mitre_mapper_service import (
    MitreMapperService
)

from app.repositories.ioc_repository import (
    IOCRepository
)

from app.repositories.mitre_repository import (
    MitreRepository
)

class ScanProcessorService:

    @staticmethod
    def process(scan_id: str):

        print(
            f"[SCAN PROCESSOR] PROCESS CALLED FOR SCAN: {scan_id}"
        )

        print(
            f"[SCAN PROCESSOR] START TIME: {datetime.utcnow()}"
        )

        # Fetch scan
        scan = ScanRepository.get_by_id(
            scan_id
        )

        if not scan:
            raise Exception(
                "Scan not found"
            )

        if not scan.get(
            "file_path"
        ):
            raise Exception(
                "Scan has no file"
            )

        # Prevent duplicate processing
        if scan.get("status") == "completed":

            print(
                f"[SCAN PROCESSOR] Scan already completed: {scan_id}"
            )

            return {
                "message":
                    "Scan already processed",
                "scan_id":
                    scan_id,
            }

        # Mark processing
        ScanRepository.update_status(
            scan_id,
            "processing"
        )

        # Download image
        local_file = (
            StorageService.download_scan(
                scan["file_path"]
            )
        )

        # OCR
        extracted_text = (
            OCRService.extract_text(
                local_file
            )
        )

        # Normalize
        normalized_text = (
            TextNormalizerService.normalize(
                extracted_text
            )
        )

        # Repair OCR artifacts
        normalized_text = (
            UrlRepairService.repair(
                normalized_text
            )
        )
        
        print("[URL REPAIR RESULT]")

        print(normalized_text)
        
        # Save OCR text
        OCRResultRepository.create(
            scan_id,
            normalized_text
        )
        
        ocr_quality = (
            OCRQualityService.analyze(
                normalized_text
            )
        )

        print(
            f"[OCR QUALITY] {ocr_quality}"
        )

        # Threat Detection
        findings = (
            ThreatDetectionService.detect(
                normalized_text
            )
        )

        # Brand Detection
        brand_hits = (
            BrandDetectionService.detect(
                normalized_text
            )
        )

        for hit in brand_hits:

            findings.append(
                {
                    "type": "brand",
                    "value": hit["brand"],
                    "confidence": hit["confidence"],
                }
            )

        # Context Analysis
        context_hits = (
            ContextAnalysisService.detect(
                normalized_text
            )
        )

        findings.extend(
            context_hits
        )

        # Domain Intelligence
        domain_hits = (
            DomainIntelligenceService.analyze(
                findings
            )
        )

        findings.extend(
            domain_hits
        )
        
        # WHOIS Domain Age Intelligence

        whois_findings = []

        for finding in findings:

            if finding["type"] != "url":
                continue

                domain = (
        finding["value"]
        .replace("http://", "")
        .replace("https://", "")
        .split("/")[0]
    )

                whois_data = (
        WhoisService.analyze(
            domain
        )
    )

                age_findings = (
        DomainAgeService.analyze(
            whois_data
        )
    )

                whois_findings.extend(
        age_findings
    )

        findings.extend(
    whois_findings
)
        
        reputation_hits = (
            DomainReputationFindingService.analyze(
            findings
            )
        )

        findings.extend(
            reputation_hits
        )

        # Threat Intelligence
        threat_intel_hits = (
            ThreatIntelligenceService.analyze(
                findings
            )
        )

        findings.extend(
            threat_intel_hits
        )

        # Final deduplication
        unique_findings = []

        seen = set()

        for finding in findings:

            key = (
                finding.get("type"),
                finding.get("value"),
            )

            if key not in seen:

                unique_findings.append(
                    finding
                )

                seen.add(key)

        findings = unique_findings

        print(
            f"[SCAN PROCESSOR] TOTAL FINDINGS: {len(findings)}"
        )

        # Save findings
        for finding in findings:

            ThreatFindingRepository.create(
                scan_id=scan["id"],
                finding_type=finding["type"],
                finding_value=finding["value"],
            )

        # Threat Score
        threat_score = (
            ThreatScoreService.calculate(
                findings
            )
        )

        ScanRepository.update_threat_score(
            scan_id,
            threat_score
        )

        # Risk Level
        risk_level = (
            RiskLevelService.get_level(
                threat_score
            )
        )

        # Classification
        classification = (
            ScamClassifierService.classify(
                findings
            )
        )
        
        # IOC Extraction

        iocs = IOCService.extract(
    findings
)

        print(
    "[SCAN PROCESSOR] IOCS:",
    len(iocs)
)

        for ioc in iocs:

            IOCRepository.create(
                scan_id=scan_id,
                ioc_type=ioc["ioc_type"],
                ioc_value=ioc["ioc_value"]
    )


        # MITRE Mapping

        mitre_techniques = (
            MitreMapperService.map(
                findings
    )
)

        print(
                "[SCAN PROCESSOR] MITRE:",
                len(mitre_techniques)
)

        for technique in mitre_techniques:

            MitreRepository.create(
                scan_id=scan_id,
                technique_id=technique["id"],
                technique_name=technique["name"]
    )
        
        from app.services.report_generator_service import (
            ReportGeneratorService
        )
        
        

        report = (
                    ReportGeneratorService.generate(
                    findings,
                    classification,
                    threat_score
    ) 
)
        
        ReportRepository.create(
    scan_id=scan["id"],
    summary=report["summary"],
    verdict=classification["scam_type"],
    confidence=classification["confidence"],
    risk_level=report["risk_level"],
    attack_vectors=report["attack_vectors"],
    recommended_actions=report["recommended_actions"]
)

        print(
    "[SCAN PROCESSOR] REPORT SAVED"
)

        print(
    "[SCAN PROCESSOR] REPORT GENERATED"
)
        
        print(
    "[SCAN PROCESSOR] REPORT:",
    report
)
        
        print("[SCAN PROCESSOR] GENERATING RISK NARRATIVE")
        
        risk_narrative = (
            RiskNarrativeService.generate(
                classification["scam_type"],
                findings,
            )
        )
        
        print("[SCAN PROCESSOR] RISK NARRATIVE CREATED")
        
        explanation = (
            ThreatExplanationService.generate(
            findings,
            classification["scam_type"],
            risk_level
            )
        )

        actions = (
                ActionRecommendationService.generate(
        classification["scam_type"]
    )
)
        
        # Recommendations
        recommendations = (
            RecommendationService.generate(
                classification["scam_type"]
            )
        )

        ClassificationRepository.create(
            scan_id=scan_id,
            scam_type=classification[
                "scam_type"
            ],
            confidence=classification[
                "confidence"
            ],
            explanation=classification[
                "explanation"
            ],
        )

        ScanRepository.update_status(
            scan_id,
            "completed"
        )

        print(
            f"[SCAN PROCESSOR] FINISHED SCAN: {scan_id}"
        )

        return {
    "scan_id": scan_id,

    "classification": classification,

    "report": report,

    "risk_level": risk_level,

    "risk_narrative": risk_narrative,

    "threat_explanation": explanation,

    "actions": actions,

    "iocs": iocs,

    "mitre": mitre_techniques,

    "recommendations": recommendations
}