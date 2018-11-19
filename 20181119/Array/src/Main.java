public class Main {

    public static void main(String[] args) {
	// write your code here
        int[] arr=new int[10];
        for (int i=0;i<10;i++){
            arr[i]=i;
        }
        int [] scores=new int[]{100,99,96};
        for(int score:scores){
            System.out.println(score);
        }
    }
}
