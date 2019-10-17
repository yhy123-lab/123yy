//全排列//
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Solution {
    private void generatePermution(int[] nums,boolean[] visited,int curSize,Stack<Integer> path,List<List<Integer>> res){
        if (curSize == nums.length){
            res.add(new ArrayList<>(path));
            return;
        }
        for(int i = 0; i < nums.length;i++){
           if(!visited[i]){
               visited[i] = true;
               path.push(nums[i]);
               generatePermution(nums,visited,curSize + 1,path,res);
               visited[i] = false;
               path.pop();
           } 
        }
    }
    public List<List<Integer>>permute(int[] nums){
        List<List<Integer>> res = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        if (nums.length == 0){
            return res;
        }
        generatePermution(nums,used,0,new Stack<>(),res);
        return res;
    }
}
