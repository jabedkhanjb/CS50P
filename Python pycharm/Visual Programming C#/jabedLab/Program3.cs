using System;

class anothermember
{
   public string uniName;
   public string student;
   public int graduationYear;
   static void printme()
   {
    Console.WriteLine("Hi, this is Mahfuz Islam Khan Jabed");
   }



}
class Program3
{
    
    static void Main()
    {
        anothermember stuAdd = new anothermember();  
        stuAdd.uniName = "The Millennium University";
        stuAdd.student = "Rewjan Islam Arpon";
        stuAdd.graduationYear = 2024;

        //Print line
        Console.WriteLine(stuAdd.uniName);
        Console.WriteLine(stuAdd.student);
        Console.WriteLine(stuAdd.graduationYear);
        anothermember newclass = new anothermember();
        

    }
}