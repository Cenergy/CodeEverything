public class LinkList<E> {


    //定义私有类,内部类

    private class Node {
        public E e;
        public Node next;

        public Node(E e, Node next) {
            this.e = e;
            this.next = next;
        }

        public Node(E e) {
            this(e, null);
        }

        public Node() {
            this(null, null);
        }

        @Override
        public String toString() {
            return e.toString();
        }
    }

    private Node dummyHead;
    private int size;

    public LinkList() {
        dummyHead = new Node(null, null);
        size = 0;
    }

    public int getSize() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void add(int index, E e) {
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("index out of control");
        } else {
            Node pre = dummyHead;
            for (int i = 0; i < index; i++) {
                pre = pre.next;
            }
            pre.next = new Node(e, pre.next);
            size++;
        }
    }

    public void addFirst(E e) {
        add(0, e);
    }

    public void addLast(E e) {
        add(size, e);
    }

    public E get(int index) {
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("index out of control");
        }
        Node cur = dummyHead.next;
        for (int i = 0; i < index; i++) {
            cur = cur.next;
        }
        return cur.e;
    }

    public E getFirst() {
        return get(0);
    }

    public E getLast() {
        return get(size - 1);
    }

    public E set(int index, E e) {
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("index out of control");
        }
        Node cur = dummyHead.next;
        for (int i = 0; i < index; i++) {
            cur = cur.next;
        }
        return cur.e = e;
    }

    public boolean contains(E e) {
        Node cur = dummyHead.next;
        while (cur.next != null) {
            if (cur.e.equals(e)) {
                return true;
            }
            cur = cur.next;
        }
        return false;
    }

    public E remove(int index) {
        if (index < 0 || index > size) {
            throw new IllegalArgumentException("index out of control");
        }
        Node prev = dummyHead;
        for (int i=0; i < index; i++) {
            prev = prev.next;
        }
        Node retNode=prev.next;
        prev.next = retNode.next;
        retNode.next = null;
        size--;
        return retNode.e;
    }
    public E removeFirst(){
        return remove(0);
    }

    public E removeLast(){
        return remove(size-1);
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
//        Node cur=dummyHead.next;
//        while (cur!=null){
//            res.append(cur+"-->");
//            cur=cur.next;
//        }
        for (Node cur = dummyHead.next; cur != null; cur = cur.next) {
            res.append(cur + "-->");
        }
        res.append("NULL");
        return res.toString();
    }

    public static void main(String[] args) {
        LinkList<Integer> linklist = new LinkList<>();
        for (int i = 0; i < 5; i++) {
            linklist.addLast(i);
        }
        linklist.add(2, 666);
        System.out.println(linklist);
        linklist.remove(2);
        System.out.println(linklist);
        linklist.removeFirst();
        System.out.println(linklist);
        linklist.removeLast();
        System.out.println(linklist);
    }

}
