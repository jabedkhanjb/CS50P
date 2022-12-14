using System;

class Program {
  public static void Main (string[] args) 
  {
    Console.WriteLine("Enter number: ");
    
    int a = Convert.ToInt32(Console.ReadLine());
    int b = Convert.ToInt32(Console.ReadLine());
    int c = Convert.ToInt32(Console.ReadLine());


    if( ( a*a + b*b == c*c) || ( c*c + b*b == a*a) ||( c*c + a*a == b*b) )
    {
        Console.WriteLine("Sides of Right angled triangle");
    }
    else 
    {
        Console.WriteLine("Mot sides of Right angled triangle");
    }




  }
  
}