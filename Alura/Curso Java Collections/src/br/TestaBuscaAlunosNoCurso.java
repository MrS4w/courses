package br;

public class TestaBuscaAlunosNoCurso {
	public static void main(String[] args) {
		Curso javaColecoes = new Curso("Dominando as coleções do Java", "Paulo Silveira");

		javaColecoes.adiciona(new Aula("Trabalhando com ArrayList", 21));
		javaColecoes.adiciona(new Aula("Criando uma aula", 20));
		javaColecoes.adiciona(new Aula("Modelando com coleções", 24));

		Aluno a1 = new Aluno("Victor Antonio", 161094333);
		Aluno a2 = new Aluno("Paulo Silveira", 1234);
		Aluno a3 = new Aluno("Bill Gates", 236596);

		javaColecoes.matricula(a1);
		javaColecoes.matricula(a2);
		javaColecoes.matricula(a3);

		System.out.println("Quem é o aluno com matricula 1234?");
		Aluno aluno = javaColecoes.buscaMatriculado(1234);
		System.out.println("aluno: " + aluno);
	}
}
