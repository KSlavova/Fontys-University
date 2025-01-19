namespace Bank
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            BankAccount account = new BankAccount();
            string client = textBox1.Text;
            int accountNo = int.Parse(textBox2.Text);
            account.InitializeBankAccount(client, accountNo);
            account.DepositMoney(double.Parse(textBox5.Text));
            if (account.WithdrawMoney(double.Parse(textBox4.Text)) == false)
            {
                MessageBox.Show("Not enough money");
            }
            else
            {
                label4.Text = account.GetInfo();
            }
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }
    }
}
