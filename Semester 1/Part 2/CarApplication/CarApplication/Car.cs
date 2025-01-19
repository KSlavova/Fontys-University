using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CarApplication
{
    public class Car
    {
        private string brand;
        private int currentSpeed;
        private int maximumSpeed;

        public void SetBrand(string brand)
        {
            this.brand = brand; 
        }

        public string GetInfo()
        {
            return $"Speed of my {brand} is {currentSpeed} and the maximum speed is {maximumSpeed}.";
        }

        public void SetMaxSpeed(int maxSpeed)
        {
            this.maximumSpeed = maxSpeed;
        }

        public void SpeedUp()
        {
            if (currentSpeed < maximumSpeed)
            {
                currentSpeed += 7;
            }
            else
            {
                currentSpeed = maximumSpeed;
            }

        }
        public void SlowDown()
        {
            if (currentSpeed >= 10)
            {
                currentSpeed -= 10;
            }
            else
            {
                currentSpeed = 0;
            }
        }
    }
}
