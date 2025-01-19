using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bank
{
    internal class BankAccount
    {
        private string client;
        private int accountNo;
        private double balance;

        

        public void InitializeBankAccount(string newClient, int newAccountNo)
        {
            this.client = newClient;
            this.accountNo = newAccountNo;
            balance = 0.0;
        }

        public void DepositMoney(double amount)
        {
            balance += amount;
        }

        public bool WithdrawMoney(double amount)
        {
            if(balance>=amount)
            {
                balance -= amount;
                return true;    
            }
            else
            {
                return false;
            }
        }

        public string GetInfo()
        {
            return $"Client {client} ({accountNo}): {balance} euro(s)";
        }
    }
}
