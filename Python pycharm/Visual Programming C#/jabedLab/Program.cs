using System;

class Program
{
    string uniName = "The millennium Univerisity";
    string student = "Mahfuz Islam Khan Jabed";
    int graduationYear = 2024;

    static void Main()
    {
        Program stuAdd = new Program();  
        Console.WriteLine("Information of a student:");      
        Console.WriteLine(stuAdd.uniName);
        Console.WriteLine(stuAdd.student);
        Console.WriteLine(stuAdd.graduationYear);
    }
}