import java.util.Random;

public class MaxHeap<E extends Comparable<E>> {
    private Array<E> data;

    public MaxHeap(int capcity) {
        data = new Array<>(capcity);
    }

    public MaxHeap() {
        data = new Array<>();
    }

    //任意数组变成MaxHeap
    public MaxHeap(E[] arr){
        data=new Array<>(arr);
        for (int i=parent(arr.length-1);i>=0;i--){
            siftDown(i);
        }
    }

    public int size() {
        return data.getSize();
    }

    public boolean isEmpty() {
        return data.isEmpty();
    }

    //返回该节点的父亲节点的索引
    private int parent(int index) {
        if (index == 0) {
            throw new IllegalArgumentException("index=0 has not parent");
        }
        return (index - 1) / 2;
    }

    //返回左孩子所在的节点索引
    private int leftChild(int index) {
        return index * 2 + 1;
    }

    private int rightChild(int index) {
        return index * 2 + 2;
    }

    //向堆中添加元素
    public void add(E e) {
        data.addLast(e);
        siftUp(data.getSize() - 1);
    }

    private void siftUp(int k) {
        while (k > 0 && data.get(parent(k)).compareTo(data.get(k)) < 0) {
            data.swap(k, parent(k));
            k = parent(k);
        }
    }
    public E findMax(){
        if(data.getSize()==0){
            throw new IllegalArgumentException("can not findMax when heap is empty");
        }
        return data.get(0);
    }
    public E extractMax(){
        E ret=findMax();
        data.swap(0,data.getSize()-1);
        data.removeLast();
        siftDown(0);
        return ret;
    }
    private void siftDown(int k){
        while (leftChild(k)<data.getSize()){
            int j=leftChild(k);
            if(j+1<data.getSize()&&data.get(j+1).compareTo(data.get(j))>0){
                j=rightChild(k);
            }
            //data[j]是leftChild和rightChild中的较大值
            if(data.get(k).compareTo(data.get(j))>=0){
                break;
            }else{
                data.swap(k,j);
                k=j;
            }
        }
    }
    //用元素e来替换最大元素
    public E replace(E e){
        E ret=findMax();
        data.set(0,e);
        siftDown(0);
        return ret;
    }


    private  static double testMaxHeap(Integer[] testData,boolean isHeapify){
        long startTime=System.nanoTime();
        MaxHeap<Integer> maxHeap;
        if(isHeapify){
            maxHeap=new MaxHeap<>(testData);
        }else{
            maxHeap=new MaxHeap<>();
            for(int num:testData){
                maxHeap.add(num);
            }
        }
//        int[] arr=new int[testData.length];
//        for(int i=0;i<testData.length;i++){
//            arr[i]=maxHeap.extractMax();
//        }
//        for (int i=1;i<testData.length;i++){
//            if(arr[i-1]<arr[i]){
//                throw new IllegalArgumentException("error");
//            }
//        }
        System.out.println("MaxHeap is complete");
        long endTime=System.nanoTime();
        return (endTime-startTime)/1000000000.0;
    }


    public static void main(String[] args) {



        int n=1000000;
        Integer[] testData=new Integer[n];
        Random random=new Random();
        MaxHeap<Integer> maxheap=new MaxHeap<>();
        for(int i=0;i<n;i++){
            testData[i]=random.nextInt(Integer.MAX_VALUE);
        }
        double time1=testMaxHeap(testData,false);
        System.out.println("maxHeap without heapify"+time1+"s");
        double time2=testMaxHeap(testData,true);
        System.out.println("maxHeap without heapify"+time2+"s");

    }

}
