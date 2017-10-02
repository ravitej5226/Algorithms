using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MaximumOfMinimumWindowSize
{
    class Program
    {
        public static void Main(string[] args)
        {
            int[] inputArray = new int[] { 10, 20, 30, 50, 10, 70, 30 };

            // Get size of array
            int inputSize = inputArray.Length;

            // initialize window size
            int windowSize = 1;

            // Calculate number of main loops possible
            int mainLoopCounter = inputSize / windowSize;
            int head = 0;
            Console.WriteLine("Window Size: " + windowSize + "\n");
            // Loop till a window size is available
            while (inputSize / windowSize > 0)
            {
                int i = 0;
                int maxOfMin = inputArray[i];
                while ((inputSize-head)>=windowSize)
                {
                   
                    int min = inputArray[head];
                    int temp = head;
                    for (int arrayHead = 0; arrayHead < windowSize; arrayHead++)
                    {
                        if (inputArray[arrayHead+head] < min)
                        {
                            min = inputArray[arrayHead+head];
                        }
                        //head++;
                    }
                    i++;
                    head=i;
                    Console.WriteLine(min + " ");

                    if(min>maxOfMin)
                    {
                        maxOfMin = min;
                    }
                }

                Console.WriteLine("Max of min: " + maxOfMin + "\n");
                
                head = 0;
                windowSize++;
                Console.WriteLine("Window Size: " + windowSize + "\n");
            }


            Console.ReadLine();


        }
    }
}
