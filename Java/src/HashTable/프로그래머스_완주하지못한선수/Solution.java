package HashTable.프로그래머스_완주하지못한선수;

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Marathon marathon = new Marathon();
        Arrays.stream(participant).forEach(marathon::addParticipant);
        Arrays.stream(completion).forEach(marathon::completeParticipant);
        return new ArrayList<>(marathon.getNotCompleted()).get(0);
    }

    class Marathon {
        private HashMap<String, Integer> members;

        public Marathon() {
            members = new HashMap<>();
        }

        public void addParticipant(String name) {
            Integer memberCount = members.getOrDefault(name, 0);
            members.put(name, memberCount + 1);
        }

        public void completeParticipant(String name) {
            try {
                Integer memberCount = members.get(name);
                if (memberCount > 1) {
                    members.put(name, memberCount - 1);
                } else {
                    members.remove(name);
                }
            } catch (Exception e) {
                throw e;
            }
        }

        public Set<String> getNotCompleted(){
            return members.keySet();
        }
    }
}



