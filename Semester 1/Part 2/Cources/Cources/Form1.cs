namespace Cources
{
    public partial class Form1 : Form
    {
        private Course course;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Create_Click(object sender, EventArgs e)
        {
            if (int.TryParse(textBox2.Text, out int ec))
            {
                course = new Course(textBox1.Text, int.Parse(textBox2.Text));
            }
            else
            {
                course = new Course(textBox1.Text);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label3.Text = $"{course.Name} {course.Ec}";
        }
    }
}
