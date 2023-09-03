"""
Tyrell Garza
JP Morgan & Chase Co.
Task 1: Analyze a Large Dataset of Fraud in Financial Payment Services.

"""

import pandas as pd
import matplotlib.pyplot as plt


def exercise_0(file):
    df = pd.read_csv(file)
    return df


def exercise_1(df):
    return df.columns.tolist()


def exercise_2(df, k):
    return df.head(k)


def exercise_3(df, k):
    return df.sample(k)


def exercise_4(df):
    return df["type"].unique().tolist()


def exercise_5(df):
    """
    Analyzes frequency of transaction(trends), monitor transaction
    flows, fruad detection (frequent unusual destinations).
    """
    return df["nameDest"].value_counts().head(10)


def exercise_6(df):
    """
    Returns fraud transactions.
    """
    return df[df["isFraud"] == 1]


def exercise_7(df):
    """
    Counts number of unique people a user has
    sent money to, sorting user by count.
    """
    return (
        df.groupby("nameOrig")["nameDest"]
        .nunique()
        .sort_values(ascending=False)
    )


def visual_1(df):
    def transaction_counts(df):
        return df["type"].value_counts()

    def transaction_counts_split_by_fraud(df):
        return df[df["isFraud"] == 1]["type"].value_counts()

    fig, axs = plt.subplots(2, figsize=(6, 10))
    transaction_counts(df).plot(ax=axs[0], kind="bar")
    axs[0].set_title("Transaction Types")
    axs[0].set_xlabel("Transaction Type")
    axs[0].set_ylabel("Count")
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind="bar")
    axs[1].set_title("Fraudulent Transaction Types")
    axs[1].set_xlabel("Transaction Type")
    axs[1].set_ylabel("Count")
    fig.suptitle("Transaction Type Analysis")
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
        for p in ax.patches:
            ax.annotate(
                p.get_height(),
                (p.get_x() + p.get_width() / 2.0, p.get_height()),
                ha="center",
                va="center",
                xytext=(0, 10),
                textcoords="offset points",
            )
    return (
        "This graph shows the distribution of transaction types,"
        "and how they relate to fraudulent transactions."
    )


def visual_2(df):
    # Filter the dataframe for 'Cash Out' transactions
    cash_out = df[
        df["type"] == "CASH_OUT"
    ].copy()  # using .copy() to prevent SettingWithCopyWarning

    # Calculate deltas for origin and destination account balances
    cash_out["origin_delta"] = abs(
        cash_out["oldbalanceOrg"] - cash_out["newbalanceOrig"]
    )
    cash_out["dest_delta"] = abs(
        cash_out["oldbalanceDest"] - cash_out["newbalanceDest"]
    )

    # Create a scatter plot
    plot = cash_out.plot.scatter(x="origin_delta", y="dest_delta")
    plot.set_title(
        "Origin vs Destination Account Balance Delta for Cash Out Transactions"
    )
    plot.set_xlabel("Origin Account Balance Delta")
    plot.set_ylabel("Destination Account Balance Delta")

    return "Change in account balances for Cash Out transactions."


def exercise_custom(df):
    """
    This function calculates two specific average values from our data.
    The average amount for all transactions and the average amount but
    only for fraudulent transactions.
    """
    # Calculate the average transaction amount for all transactions
    average_trans = df["amount"].mean()

    # Calculate the average transaction amount for only fraudulent transactions
    average_fraud_trans = df[df["isFraud"] == 1]["amount"].mean()

    return average_trans, average_fraud_trans


def visual_custom(df):
    """

    This function visualizes the data from exercise_custom. Creates a bar chart
    that shows the average transaction amounts: one bar for all transactions
    and one bar for just the fraudulent ones.
    """
    average_trans, average_fraud_trans = exercise_custom(df)

    # Data for bar plot
    labels = ["All Transactions", "Fraudulent Transactions"]
    values = [average_trans, average_fraud_trans]

    # Creating the bar plot
    plt.bar(labels, values)

    # Setting the title and labels
    plt.title("Average Amounts: All vs. Fraudulent Transactions")
    plt.ylabel("Amount")

    # Displaying the bar chart
    plt.show()


def main():
    df = exercise_0("transactions.csv")
    print(df.head(10))

    column_names = exercise_1(df)
    print(column_names)
    print(exercise_2(df, 5))
    print(exercise_3(df, 5))
    print(exercise_4(df))
    print(exercise_5(df))
    print(exercise_6(df))
    print(exercise_7(df))

    """description_1 = visual_1(df)
    print(description_1)
    plt.show()

    description_2 = visual_2(df)
    print(description_2)
    plt.show()"""

    # Calling the custom functions
    custom_data = exercise_custom(df)
    print("Average Transaction Amounts:")
    print(custom_data[0])
    print("\nAverage Fraudulent Transaction Amounts:")
    print(custom_data[1])

    visual_custom(df)


if __name__ == "__main__":
    main()
