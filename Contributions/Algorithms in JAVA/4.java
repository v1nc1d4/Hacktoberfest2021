import java.util.Scanner;
class Q4{
	public static void main(String[] args)
	{
		Scanner r=new Scanner(System.in);
		System.out.println("Enter a string: ");
		String str=r.nextLine();
		String strRev="";
		for(int i=str.length()-1;i>=0;i--){	
			strRev+=str.charAt(i);
		}
		if(str.equals(strRev)) System.out.println("It is a Palindrome!");
		else System.out.println("Not a Palindrome!");
		r.close();
	}
} 
