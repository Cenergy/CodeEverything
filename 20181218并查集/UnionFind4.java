public class UnionFind4 implements UF {
    private int[] parent;
    private int[] rank;

    public UnionFind4(int size) {
        parent = new int[size];
        rank = new int[size];
        for (int i = 0; i < size; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
    }

    @Override
    public int getSize() {
        return parent.length;
    }

    private int find(int p) {
        if (p < 0 && p > parent.length) {
            throw new IllegalArgumentException("p is out of bound");
        }
        while (p != parent[p]) {
            p = parent[p];
        }
        return p;
    }

    @Override
    public boolean isConnected(int q, int p) {
        return find(q) == find(p);
    }

    @Override
    public void unionElement(int q, int p) {
        int qRoot = find(q);
        int pRoot = find(p);
        if (qRoot == pRoot) {
            return;
        } else {
            //将元素少的合并到元素多的上
            if (rank[qRoot] > rank[pRoot]) {
                parent[pRoot] = qRoot;
            } else if (rank[qRoot] < rank[pRoot]) {
                parent[qRoot] = pRoot;
            } else {//rank[qRoot] == rank[pRoot
                parent[qRoot] = pRoot;
                rank[pRoot] += 1;
            }
        }
    }

    public static void main(String[] args) {
        System.out.println("123");
    }
}
