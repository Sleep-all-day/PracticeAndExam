import java.util.ArrayList;
import java.util.List;

public class No_6 {
    public String z(String s, int numRows){
        if(numRows == 1)return s;

        int curRow = 0;
        boolean direction = true;
        int allRows = Math.min(s.length(), numRows);
        List<StringBuilder> rowsArray = new ArrayList<StringBuilder>();
        for(int i = 0; i < allRows; i++){
            rowsArray.add(new StringBuilder());
        }


        for(char c : s.toCharArray()){
            rowsArray.get(curRow).append(c);
            //如果到了首行
            if(curRow == 0){
                direction = true;
                curRow++;
            }
            //如果到了末行
            else if(curRow == allRows - 1){
                direction = false;
                curRow--;
            }
            //如果在中间行
            else {
                if(direction)curRow++;
                else curRow--;
            }
        }
        StringBuilder res = new StringBuilder();
        for(StringBuilder rowArray: rowsArray){
            res.append(rowArray);
        }

        return res.toString();
    }
}
