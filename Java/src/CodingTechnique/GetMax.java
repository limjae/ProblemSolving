package CodingTechnique;

import java.util.Arrays;
import java.util.stream.Collectors;

public class GetMax {
    public void max(){
        Integer[] distances2 = new Integer[10 + 1];

        Integer max = Arrays.stream(distances2).mapToInt(Integer::intValue).max().getAsInt();

    }
}
