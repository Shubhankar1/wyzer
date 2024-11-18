class DCFModel:
    def calculate_dcf(self, free_cash_flows, discount_rate, terminal_growth_rate, net_debt, shares_outstanding):
        """
        Calculate intrinsic stock value using DCF.
        """
        try:
            projected_cash_flows = [fcf * (1 + terminal_growth_rate) for fcf in free_cash_flows]
            terminal_value = projected_cash_flows[-1] / (discount_rate - terminal_growth_rate)
            discounted_cash_flows = [
                cf / ((1 + discount_rate) ** i) for i, cf in enumerate(projected_cash_flows, 1)
            ]
            equity_value = sum(discounted_cash_flows) + terminal_value - net_debt
            intrinsic_value = equity_value / shares_outstanding
            return intrinsic_value
        except Exception as e:
            print(f"Error calculating DCF: {e}")
            return 0

