from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime
import os


class DecisionReportGenerator:
    def generate(
        self,
        output_path,
        application_data,
        result_summary,
        chart_path
    ):
        styles = getSampleStyleSheet()
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=36,
            leftMargin=36,
            topMargin=36,
            bottomMargin=36
        )

        elements = []

        # ===============================
        # TITLE
        # ===============================
        elements.append(Paragraph(
            "<b>Credit Decision Memory – Similarity-Based Assessment</b>",
            styles["Title"]
        ))
        elements.append(Spacer(1, 12))

        elements.append(Paragraph(
            f"<b>Date:</b> {datetime.today().strftime('%d %B %Y')}",
            styles["Normal"]
        ))
        elements.append(Paragraph(
            "<b>Team:</b> Weavers",
            styles["Normal"]
        ))
        elements.append(Spacer(1, 20))

        # ===============================
        # APPLICATION SUMMARY
        # ===============================
        elements.append(Paragraph(
            "<b>1. Loan Application Overview</b>",
            styles["Heading2"]
        ))
        elements.append(Spacer(1, 8))

        app_table = Table([
            ["Monthly Income", f"${application_data['monthly_income']:.0f}"],
            ["Loan Amount Requested", f"${application_data['loan_amount_requested']:.0f}"],
            ["Loan Tenure (months)", application_data["loan_tenure_months"]],
            ["Credit Score", application_data["cibil_score"]],
            ["Loan Purpose", application_data["purpose_of_loan"]],
        ], colWidths=[220, 250])

        app_table.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
        ]))

        elements.append(app_table)
        elements.append(Spacer(1, 20))

        # ===============================
        # SIMILARITY FINDINGS
        # ===============================
        elements.append(Paragraph(
            "<b>2. Similarity-Based Evidence</b>",
            styles["Heading2"]
        ))
        elements.append(Spacer(1, 8))

        elements.append(Paragraph(
            f"The system retrieved <b>{result_summary['total_cases']}</b> historical loan cases "
            f"with similar financial characteristics (income, loan size, credit score, and purpose). "
            f"This analysis relies on historical outcomes rather than predictive modeling.",
            styles["Normal"]
        ))
        elements.append(Spacer(1, 12))

        # ===============================
        # OUTCOME TABLE
        # ===============================
        outcome_table = Table([
            ["Outcome", "Percentage of Similar Cases"],
            ["Repaid", f"{result_summary['repaid_pct']:.1f}%"],
            ["Defaulted", f"{result_summary['defaulted_pct']:.1f}%"],
            ["In Progress", f"{result_summary['in_progress_pct']:.1f}%"],
        ], colWidths=[220, 250])

        outcome_table.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
        ]))

        elements.append(outcome_table)
        elements.append(Spacer(1, 20))

        # ===============================
        # CHART IMAGE
        # ===============================
        if os.path.exists(chart_path):
            elements.append(Paragraph(
                "<b>3. Outcome Distribution Visualization</b>",
                styles["Heading2"]
            ))
            elements.append(Spacer(1, 8))
            elements.append(Image(chart_path, width=350, height=350))
            elements.append(Spacer(1, 20))

        # ===============================
        # INTERPRETATION
        # ===============================
        elements.append(Paragraph(
            "<b>4. Interpretation & Decision Support</b>",
            styles["Heading2"]
        ))
        elements.append(Spacer(1, 8))

        elements.append(Paragraph(
            "A higher proportion of repaid loans among similar historical cases suggests "
            "lower observed repayment risk. Conversely, elevated default or fraud presence "
            "indicates increased caution. This report is intended to support human decision-making "
            "and does not automate approval or rejection.",
            styles["Normal"]
        ))

        doc.build(elements)
