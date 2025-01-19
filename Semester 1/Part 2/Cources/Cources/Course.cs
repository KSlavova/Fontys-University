using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cources
{
    public class Course
    {
        public string Name { get; set; }
        public int Ec { get; set; }

        public Course(string name, int ec)
        {
            Name = name;
            Ec = ec;    
        }

        public Course(string name)
        {
            Name = name;
            Ec = 3;
        }
    }
}
