class Shape  // base class (parent) 
{
   public int height;
   public int width;
}
class Triange : Shape
{
    public void AreaT (int h, int w)
    {
        Console.WriteLine("Area of Triangle: "+ h*w*(1/2));
    }
}
class rectange : Shape
{
    public rectange(int height, int width)
    {
        this.height = height;
        this.width = width;
    }
    public  void AreaR ()
    {
        Console.WriteLine("Area of rectangle: "+ height*width);
    }
}
class Program
{
  static void Main(string[] args)
  {
    Triange t = new Triange();
    t.height = 20;
    t.width = 34;
    t.AreaT(t.height,t.width);
    rectange r = new rectange(20,34);
  }
}