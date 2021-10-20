import java.util.Scanner;
class Q5{
	public static void main(String[] args)
	{
		Scanner r=new Scanner(System.in);
		System.out.println("Enter a string: ");
		String str=r.nextLine();
		str = str.replaceAll("\\s", "");
		int[] data = new int[26];
		for(int i=0;i<str.length();i++){
			int asci = str.charAt(i);	
			data[asci-97]++;
		}
		boolean yes = true;
		for(int i=0; i<26;i++){
			if(data[i]==0){
				yes = false;break;
			}
		}
		if(yes) System.out.println("It is a Pangram");
		else  System.out.println("Not a Pangram");
		r.close();
	}
} 
