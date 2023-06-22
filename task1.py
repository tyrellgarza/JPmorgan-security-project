'''
Tyrell Garza
JP Morgan & Chase Co.
Task 1: Analyze a Large Dataset of Fraud in Financial Payment Services.

'''

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
    return df['type'].unique().tolist()


def exercise_5(df):
    '''
    Analyzes frequency of transaction(trends), monitor transaction
    flows, fruad detection (frequent unusual destinations).
    '''
    return df['nameDest'].value_counts().head(10)


def exercise_6(df):
    '''
    Returns fraud transactions.
    '''
    return df[df['isFraud'] == 1]


def exercise_7(df):
    '''
    Counts number of unique people a user has
    sent money to, sorting user by count.
    '''
    return df.groupby(
        'nameOrig')['nameDest'].nunique().sort_values(ascending=False)


def visual_1(df):
    def transaction_counts(df):
        # TODO
        pass

    def transaction_counts_split_by_fraud(df):
        # TODO
        pass

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('TODO')
    axs[0].set_xlabel('TODO')
    axs[0].set_ylabel('TODO')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('TODO')
    axs[1].set_xlabel('TODO')
    axs[1].set_ylabel('TODO')
    fig.suptitle('TODO')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return 'TODO'
 

'''def visual_2(df):
   # pass

def exercise_custom(df):
    #pass

def visual_custom(df):
    pass '''


def main():
    df = exercise_0('transactions.csv')
    print(df.head(10))

    column_names = exercise_1(df)
    print(column_names)
    print(exercise_2(df, 5))
    print(exercise_3(df, 5))
    print(exercise_4(df))
    print(exercise_5(df))
    print(exercise_6(df))
    print(exercise_7(df))


if __name__ == "__main__":
    main()
