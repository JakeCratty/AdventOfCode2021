void setup() {
  size(500, 500);
  background(50);
  fill(255, 0, 0);
  
  String[] input = loadStrings("input.txt");
  ArrayList<PVector> dots = new ArrayList();
  ArrayList<String> folds = new ArrayList();
  for(String s : input) {
    if(s.contains(",")) {
      String[] coords = s.split(",");
      dots.add(new PVector(Integer.valueOf(coords[0]), Integer.valueOf(coords[1])));
    }
    else if(s.contains("x") || s.contains("y"))
      folds.add(s);
  }
  
  for(String fold : folds) {
    String[] foldInfo = fold.split("=");
    char dimension = foldInfo[0].charAt(foldInfo[0].length()-1);
    int position = Integer.valueOf(foldInfo[1]);
    for(PVector dot : dots) { 
      if(dimension == 'x') { //vertical fold 
        if(dot.x > position)
          dot.x = position * 2 - dot.x;
        else if(dot.x == position)
          dot.x = -1;
      }
      else {
        if(dot.y > position) //horizontal
          dot.y = position * 2 - dot.y;
        else if(dot.y == position)
          dot.y = -1;
      }
    }
  }
  for(PVector dot : dots) {
    ellipse(dot.x*10+width/2-200, dot.y*10+height/2, 10, 10);
  }
}
