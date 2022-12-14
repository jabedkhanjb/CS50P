using System;
class Program

{
    static void Main(){
        Console.WriteLine("Enter a year: ");
        var year = Console.ReadLine();
        int b = Convert.ToInt32(year);

        if ( b % 400 == 0)
        {
            Console.WriteLine("This is leap year");
        }

        else
            {
               
            if ( b % 4 == 0)
            {
                if (b % 100 != 0 )
                Console.WriteLine("This is leap year");

                else
                {
                    Console.WriteLine("this is not leap year");
                }
            }
                else
                {
                    Console.WriteLine("this is not leap year");
                }
            }
       
    }
    
}