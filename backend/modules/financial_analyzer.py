class FinancialAnalyzer:
    def __init__(self):
        pass

    def calculate_ratios(self, financial_data):
        """
        Calculate financial ratios such as ROE and Debt-to-Equity.
        """
        try:
            ratios = {
                "Debt-to-Equity Ratio": financial_data["Total Liabilities"] / financial_data["Equity"],
                "ROE (%)": (financial_data["Net Income"] / financial_data["Equity"]) * 100,
            }
            return ratios
        except Exception as e:
            print(f"Error calculating financial ratios: {e}")
            return {}

    def calculate_npv(self, cash_flows, discount_rate):
        """
        Calculate Net Present Value (NPV) of future cash flows.
        """
        try:
            npv = sum(cash_flow / ((1 + discount_rate) ** i) for i, cash_flow in enumerate(cash_flows, 1))
            return npv
        except Exception as e:
            print(f"Error calculating NPV: {e}")
            return 0

