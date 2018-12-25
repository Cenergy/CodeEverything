import java.util.ArrayList;
public class RBTree<K extends Comparable<K>, V>{
    private static final boolean RED=true;
    private static final boolean BLACK=false;
    private class Node {
        public K key;
        public V value;
        public Node left;
        public Node right;
        public boolean color;

        public Node(K key, V value) {
            this.key = key;
            this.value = value;
            this.right = null;
            this.left = null;
            color=RED;
        }
    }

    private Node root;
    private int size;

    public RBTree() {
        root = null;
        size = 0;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int getSize() {
        return size;
    }

    public boolean isRed(Node node){
        if(node==null){
            return BLACK;
        }
        return node.color;
    }
    //     node                          x
    //      /\           左旋转           /\
    //     T1 x       ------------->  node T3
    //        /\                        /\
    //       T2 T3                     T1 T2

    private Node leftRotate(Node node){
        Node x=node.right;
        x.left=node;
        x.color=node.color;
        node.color=RED;
        return x;

    }
    private Node rightRotate(Node node){
        Node x=node.left;
        x.right=node;
        x.color=node.color;
        node.color=RED;
        return x;
    }

    private void filpColors(Node node){
        node.color=RED;
        node.left.color=BLACK;
        node.right.color=BLACK;
    }

    //向红黑树中添加元素
    public void add(K key, V value) {
        root=add(root, key, value);
        root.color=BLACK;
    }
    //向以node为根的红黑树中添加元素（key，value），递归算法。
    // 返回插入新节点后红黑树的根
    private Node add(Node node, K key, V value) {
        if (node == null) {
            size++;
            return new Node(key, value);   //默认插入红色的节点
        }
        if (key.compareTo(node.key) < 0) {
            node.left = add(node.left, key, value);
        } else if (key.compareTo(node.key) > 0) {
            node.right = add(node.right, key, value);
        } else {
            node.value = value;
        }
        if(isRed(node.right)&&!isRed(node.left)){
            node=leftRotate(node);
        }
        if(isRed(node.left)&&isRed(node.left.left)){
            node=rightRotate(node);
        }
        if(isRed(node.right)&&isRed(node.left)){
            filpColors(node);
        }
        return node;
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
