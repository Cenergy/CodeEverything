import java.util.ArrayList;
public class AVLTree<K extends Comparable<K>, V>{
    private class Node {
        public K key;
        public V value;
        public Node left;
        public Node right;
        public int height;

        public Node(K key, V value) {
            this.key = key;
            this.value = value;
            this.right = null;
            this.left = null;
            this.height=1;
        }
    }

    private Node root;
    private int size;

    public AVLTree() {
        root = null;
        size = 0;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int getSize() {
        return size;
    }

    public void add(K key, V value) {
        add(root, key, value);
    }

    private Node add(Node node, K key, V value) {
        if (node == null) {
            size++;
            return new Node(key, value);
        }
        if (key.compareTo(node.key) < 0) {
            node.left = add(node.left, key, value);
        } else if (key.compareTo(node.key) > 0) {
            node.right = add(node.right, key, value);
        } else {
            node.value = value;
        }
        node.height=1+Math.max(getHeight(node.right),getHeight(node.left));
        int bf=balanceFactor(node);
        if(Math.abs(bf)>1){
            System.out.println("unbanlance");
        }
        //平衡维护LL
        if(bf>1&&balanceFactor(node.left)>=0){
            return rightRotate(node);
        }
        //RR
        if(bf<-1&&balanceFactor(node.right)<=0){
            return leftRotate(node);
        }
        //LR
        if(bf>1&&balanceFactor(node.left)<0){
            node.left=leftRotate(node.left);
            return rightRotate(node.right);
        }

        //RL
        if(bf<-1&&balanceFactor(node.right)>0){
            node.left=rightRotate(node.left);
            return rightRotate(node.right);
        }

        return node;
    }

    //获得node的平衡因子

    private int balanceFactor(Node node){
        if(node==null){
            return 0;
        }
        return getHeight(node.left)-getHeight(node.right);
    }
    //判断是否是一颗二分搜索树
    public boolean isBST(){
        ArrayList<K> keys=new ArrayList<>();
        inOrder(root,keys);
        for(int i=0;i<keys.size();i++){
            if(keys.get(i-1).compareTo(keys.get(i))<0){
                return false;
            }
        }
        return true;
    }
    //右旋转
    //      y
    //     / \                             x
    //    x  T4      向右旋转(y)           /  \
    //   / \      --------------->       z    y         T1<z<T2<x<T3<y<T4
    //  z   T3                          / \   /\
    // / \                             T1 T2 T3 T4
    //T1 T2
    private Node rightRotate(Node y){
            Node x=y.left;
            Node T3=x.right;

            //向右旋转
            x.right=y;
            y.left=T3;
            //更新height
            y.height=Math.max(getHeight(y.left),getHeight(y.right))+1;
            x.height=Math.max(getHeight(x.left),getHeight(x.right))+1;
            return x;


    }
    //左旋转
    private Node leftRotate(Node y){
        Node x=y.right;
        Node T3=x.left;
        x.left=y;
        y.right=T3;
        //更新height
        y.height=Math.max(getHeight(y.left),getHeight(y.right))+1;
        x.height=Math.max(getHeight(x.left),getHeight(x.right))+1;
        return x;

    }
    public boolean isBalance(){
        return isBalance(root);
    }
    private boolean isBalance(Node node){
        if(node==null){
            return true;
        }
        int b=balanceFactor(node);
        if(Math.abs(b)>1){
            return false;
        }
        return isBalance(node.left)&&isBalance(node.right);

    }
    private void inOrder(Node node,ArrayList<K> keys){
        if(node==null){
            return;
        }else{
            inOrder(node.left,keys);
            keys.add(node.key);
            inOrder(node.right,keys);
        }

    }

    //    返回以node为根节点中key所在的节点
    private Node getNode(Node node, K key) {
        if (node == null) {
            return null;
        }
        if (key.compareTo(node.key) == 0) {
            return node;
        } else if (key.compareTo(node.key) < 0) {
            return getNode(node.left, key);
        } else {
            return getNode(node.right, key);
        }
    }
    private int getHeight(Node node){
        if(node==null){
            return 0;
        }
        return node.height;
    }

    public boolean contains(K key) {
        return getNode(root, key) != null;
    }

    public V get(K key) {
        Node node = getNode(root, key);
        return node == null ? null : node.value;
    }

    public void set(K key, V value) {
        Node node = getNode(root, key);
        if (node == null) {
            throw new IllegalArgumentException(key + "does not exist!!");
        } else {
            node.value = value;
        }

    }

    public V remove(K key) {
        Node node=getNode(root,key);
        if (node!=null) {
            root=remove(root,key);
            return node.value;
        } else
            return null;
    }

    //返回以node为节点的二分搜索树最小值所在的节点
    private Node minimum(Node node) {
        if (node.left == null) {
            return node;
        } else {
            return minimum(node.left);
        }
    }
    private Node removeMin(Node node) {
        if (node.left == null) {
            Node rightNode = node.right;
            node.right = null;
            size--;
            return rightNode;
        }
        node.left = removeMin(node.left);
        return node;
    }

    private Node remove(Node node, K key) {
        if (node == null) {
            return null;
        }
        if (key.compareTo(node.key) < 0) {
            node.left = remove(node.left, key);
            return node;
        } else if (key.compareTo(node.key) > 0) {
            node.right = remove(node.right, key);
            return node;
        } else {
            //e==node.e
            if (node.left == null) {
                Node rightNode = node.right;
                node.right = null;
                size--;
                return rightNode;
            } else if (node.right == null) {
                Node leftNode= node.left;
                node.left = null;
                size--;
                return leftNode;
            } else {
                Node successor = minimum(node.right);

                successor.right = removeMin(node.right);
                successor.left = node.left;

                node.right = node.right = null;
                return successor;
            }

        }

    }

    public static void main(String[] args) {
        System.out.println("123");
    }
}
