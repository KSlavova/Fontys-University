namespace CarApplication
{
    public partial class Form1 : Form
    {
        private Car myCar;
        private Car mySecondCar;


        public Form1()
        {
            InitializeComponent();
        }

        private void SpeedFirstCar_Click(object sender, EventArgs e)
        {
            myCar.SetBrand(Brand1.Text);
            myCar.SetMaxSpeed(int.Parse(Speed1.Text));
            myCar.SpeedUp();
            InfoFirstCar.Text = myCar.GetInfo();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            myCar = new Car();
            mySecondCar = new Car();
        }


        private void SlowFirstCar_Click(object sender, EventArgs e)
        {
            myCar.SlowDown();
            InfoFirstCar.Text = myCar.GetInfo();
        }

        private void SpeedSecondCar_Click(object sender, EventArgs e)
        {
            mySecondCar.SetBrand(Brand2.Text);
            mySecondCar.SetMaxSpeed(int.Parse(Speed2.Text));
            mySecondCar.SpeedUp();
            InfoSecondCar.Text = mySecondCar.GetInfo();
        }

        private void SlowSecondCar_Click(object sender, EventArgs e)
        {
            mySecondCar.SlowDown();
            InfoSecondCar.Text = mySecondCar.GetInfo();
        }

        private void InfoFirstCar_Click(object sender, EventArgs e)
        {

        }
    }
}
