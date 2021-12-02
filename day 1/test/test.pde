void setup()
{
  String[] input = loadStrings("input.txt");
  int count = 0;
  int index = 1;
  while(index <= input.length - 3)
  {
    int currentSum = 0;
    for(int i = index; i < index + 3; i++)
    {
      currentSum += Integer.valueOf(input[i]);
    }
    int previousSum = 0;
    for(int i = index - 1; i < index + 2; i++)
    {
      previousSum += Integer.valueOf(input[i]);
    }
    if(currentSum > previousSum)
      count++;
      
    index++;
  }
  println("Count: " + count);
}
