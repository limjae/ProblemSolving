package CodingTechnique;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

public class GetMax {
    public void max(){
        Integer[] distances2 = new Integer[10 + 1];
        ;
        new ArrayList<>(Arrays.asList(1,2,3,4));
        Integer max = Arrays.stream(distances2).mapToInt(Integer::intValue).reduce(Integer::max).getAsInt();

    }
}
