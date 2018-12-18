public class UnionFind2 implements UF {
    private int[] parent;

    public UnionFind2(int size) {
        parent = new int[size];
        for (int i = 0; i < size; i++) {
            parent[i] = i;
        }
    }

    @Override
    public int getSize() {
        return parent.length;
    }
    private int find(int p){
        if(p<0&&p>parent.length){
            throw new IllegalArgumentException("p is out of bound");
        }
        while (p!=parent[p]){
            p=parent[p];
        }
        return p;
    }

    @Override
    public boolean isConnected(int q, int p) {
        return find(q)==find(p);
    }

    @Override
    public void unionElement(int q, int p) {
        int qRoot=find(q);
        int pRoot=find(p);
        if(qRoot==pRoot){
            return;
        }else{
            parent[qRoot]=pRoot;
        }
    }

    public static void main(String[] args) {
        System.out.println("123");
    }
}
