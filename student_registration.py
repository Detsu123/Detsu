import java.util.ArrayList;
import java.util.List;

public class Student {
    private String id;
    private String name;
    private int age;

    public Student(String id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    @Override
    public String toString() {
        return "Student{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}

class StudentRegistration {
    private List<Student> students = new ArrayList<>();

    public void addStudent(String id, String name, int age) {
        students.add(new Student(id, name, age));
    }

    public void removeStudent(String id) {
        students.removeIf(student -> student.getId().equals(id));
    }

    public void listAllStudents() {
        for (Student student : students) {
            System.out.println(student);
        }
    }

    public static void main(String[] args) {
        StudentRegistration registration = new StudentRegistration();
        registration.addStudent("1", "John Doe", 20);
        registration.addStudent("2", "Jane Smith", 22);

        System.out.println("All Students:");
        registration.listAllStudents();

        registration.removeStudent("1");
        System.out.println("After removal:");
        registration.listAllStudents();
    }
}
