public class Array {
    private int[] data;
    private int size;
    public Array(int capacity){
        data=new int[capacity];
        size=0;
    }
    public Array(){
        data=new int[10];
    }
    public  int getSize(){
        return size;
    }
    public  int getCapacity(){
        return data.length;
    }
    public boolean isEmpty(){
        return  size==0;
    }

    public void addList(int e){
        if(size=data.length)
            throw new IllegalArgumentException("add Failed,size is full");
        data[size++]=e;
    }
    public void add(int index,int e){
        if(size=data.length)
            throw new IllegalArgumentException("add Failed,size is full");

        if
    }

}
