
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def generate_weekly_report():

    data = {
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"],
        "Sales": [12000, 15000, 13500, 18000, 22000, 25000, 20000],
        "Customers": [45, 52, 48, 60, 75, 85, 70]
    }

    df = pd.DataFrame(data)

    total_sales = df["Sales"].sum()
    average_sales = df["Sales"].mean()
    total_customers = df["Customers"].sum()
    average_customers = df["Customers"].mean()

    pdf = PdfPages("Automated_Weekly_Report.pdf")

    # Summary
    fig = plt.figure(figsize=(8.27, 11.69))
    plt.axis("off")

    report_text = f"""
GROWFINIX
AUTOMATED WEEKLY BUSINESS REPORT

Total Sales: ₹{total_sales:,.2f}
Average Daily Sales: ₹{average_sales:,.2f}

Total Customers: {total_customers}
Average Daily Customers: {average_customers:.2f}

Best Sales Day: {df.loc[df["Sales"].idxmax(), "Day"]}
Highest Sales: ₹{df["Sales"].max():,.2f}

Report Generated Automatically
"""

    plt.text(0.1, 0.85, report_text,
             fontsize=16,
             verticalalignment="top")

    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)

    # Sales chart
    fig = plt.figure(figsize=(11, 6))
    plt.plot(df["Day"], df["Sales"], marker="o")
    plt.title("Weekly Sales Report")
    plt.xlabel("Day")
    plt.ylabel("Sales (₹)")
    plt.grid(True)

    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)

    # Customer chart
    fig = plt.figure(figsize=(11, 6))
    plt.bar(df["Day"], df["Customers"])
    plt.title("Daily Customer Report")
    plt.xlabel("Day")
    plt.ylabel("Customers")

    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)

    pdf.close()

    print("Weekly report generated successfully!")


if __name__ == "__main__":
    generate_weekly_report()
