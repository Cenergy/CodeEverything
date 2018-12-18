public class UnionFind1 implements UF {
    private int[] id;
    public UnionFind1(int size){
        id=new int[size];
        for(int i=0;i<id.length;i++){
            id[i]=i;
        }
    }
    @Override
    public int getSize(){
         return id.length;
    }
    //查找元素p所属的集合编号
    private  int find(int p){
        if(p<0&&p>id.length){
            throw new IllegalArgumentException("p is out of bound");
        }
        return id[p];
    }

    @Override
    public boolean isConnected(int q, int p) {
        return find(p)==find(q);
    }

    @Override
    public void unionElement(int q, int p) {
        int pID=find(p);
        int qID=find(q);
        if(pID==qID){
            return;
        }else{
            for(int i=0;i<id.length;i++){
                if(id[i]==pID){
                    id[i]=qID;
                }
            }
        }
    }
}
