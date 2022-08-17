package CodingTechnique;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.util.stream.Stream;

public class StreamApi {
    public static void main(String[] args) {
        //https://mangkyu.tistory.com/112

        String[] nameArr = {"IronMan", "Captain", "Hulk", "Thor"};
        List<String> nameList = Arrays.asList(nameArr);

        List<String> nameList2 = nameList.stream().sorted(Comparator.naturalOrder()).collect(Collectors.toList());

        System.out.println("nameList.toString() = " + nameList.toString());
        System.out.println("nameList2.toString() = " + nameList2.toString());

        Stream<String> nameStream = nameList.stream();
        nameStream.forEach(System.out::println);
        // can use only one time
        // nameStream.forEach(System.out::println);

        create();
    }

    public static void create(){
        // Collection으로부터 생성
        List<String> stringList = new ArrayList<>(Arrays.asList("a", "b", "c"));
        Stream<String> listStream = stringList.stream();

        // 배열로부터 스트림을 생성
        Stream<String> stream1 = Stream.of("a", "b", "c"); //가변인자
        Stream<String> stream2 = Stream.of(new String[] {"a", "b", "c"});
        Stream<String> stream3 = Arrays.stream(new String[] {"a", "b", "c"});
        Stream<String> stream4 = Arrays.stream(new String[] {"a", "b", "c"}, 0, 3); //end범위 포함 x

        // 원시 스트림
        // 4이상 10 이하의 숫자를 갖는 IntStream
        IntStream intStream = IntStream.range(4, 10);
        LongStream longStream = LongStream.of(1L, 2L, 3L, 5L, 9L);
    }

    public static void modify(){
        List<String> stringList = Arrays.asList("a", "b", "c", "a", "b1", "abc");

        Stream<String> filterStream = stringList.stream().filter(name -> name.contains("a"));
        Stream<String> mapStream = stringList.stream().map(String::toUpperCase);

        Stream<String> sortedStream1 = stringList.stream().sorted();
        Stream<String> sortedStream2 = stringList.stream().sorted(new CustomComparator<>());
        Stream<String> sortedStream3 = stringList.stream().sorted(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return 0;
            }
        });


    }
}

class CustomComparator<String> implements Comparator{

    @Override
    public int compare(Object o1, Object o2) {
        return 0;
    }
}
