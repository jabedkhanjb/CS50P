//program 2
using System;

class ourmember
{
   public string uniName = "The millennium Univerisity";
   public string student = "Mahfuz Islam Khan Jabed";
   public int graduationYear = 2024;



}
class Program
{
    
    static void Main()
    {
        ourmember stuAdd = new ourmember();  
        Console.WriteLine("Information of a student:");      
        Console.WriteLine(stuAdd.uniName);
        Console.WriteLine(stuAdd.student);
        Console.WriteLine(stuAdd.graduationYear);
    }
}