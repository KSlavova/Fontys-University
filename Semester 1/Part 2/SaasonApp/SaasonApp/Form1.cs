namespace SaasonApp
{
    public partial class Form1 : Form
    {
        private Season season;
        public Form1()
        {
            InitializeComponent(); 
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if ((int)season > 3)
            {
                season = 0;
            }
            label1.Text=season.ToString();
            season++;
        }
    }
}
