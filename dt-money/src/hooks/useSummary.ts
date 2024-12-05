import { useContext } from "react";
import { TransactionContext } from "../contexts/TransactionsContext";

export function useSumary() {
    const { transactions } = useContext(TransactionContext)

    const summary = transactions.reduce(
        (acc, transaction) => {
            const price = parseFloat(transaction.price);
            if (transaction.type === 'income'){
                acc.income += price;
                acc.total += price;
            } else {
                acc.outcome += price;
                acc.total -= price;
            }
            return acc;
        }, 
        {
            income: 0,
            outcome: 0,
            total: 0
        }
    )
    return summary
}