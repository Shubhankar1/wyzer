class ComplianceChecker:
    def __init__(self, esg_data, standards):
        """
        Initialize with ESG data and standards.
        """
        self.esg_data = esg_data
        self.standards = standards

    def check_eu_taxonomy(self):
        """
        Validate ESG data against EU Taxonomy standards.
        """
        try:
            required_metrics = self.standards.get("EU", [])
            missing_metrics = [metric for metric in required_metrics if metric not in self.esg_data]
            return {
                "compliant": len(missing_metrics) == 0,
                "missing_metrics": missing_metrics
            }
        except Exception as e:
            print(f"Error in EU Taxonomy compliance check: {e}")
            return {"compliant": False, "missing_metrics": []}

    def check_sec_climate_rule(self):
        """
        Validate ESG data against SEC climate-related disclosure requirements.
        """
        try:
            required_metrics = self.standards.get("SEC", [])
            missing_metrics = [metric for metric in required_metrics if metric not in self.esg_data]
            return {
                "compliant": len(missing_metrics) == 0,
                "missing_metrics": missing_metrics
            }
        except Exception as e:
            print(f"Error in SEC compliance check: {e}")
            return {"compliant": False, "missing_metrics": []}

