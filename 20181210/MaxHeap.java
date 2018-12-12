public class MaxHeap<E extends Comparable<E>> {
    private Array<E> data;

    public MaxHeap(int capcity) {
        data = new Array<>(capcity);
    }

    public MaxHeap() {
        data = new Array<>();
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
            throw new IllegalArgumentException("can not findMax when heap is empty")
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
    //当不存在子节点时停止：
        while (leftChild(k)<data.getSize()){
            int j=leftChild(k);
            if(j+1<data.getSize()&&data.get(j+1).compareTo(data.get(i))>0){
                j=rightChild(k);
            }
            if(data.get(k).compareTo(data.get(j))>=){
                break;
            }else{
                data.swap(k,j);
                k=j;
            }
        }
    }

}
