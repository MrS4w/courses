package br;

import java.util.Iterator;
import java.util.Set;

public class TestaCursoComAluno {
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

		System.out.println("Todos os alunos matriculados: ");

		Set<Aluno> alunos = javaColecoes.getAlunos();
		Iterator<Aluno> iterador = alunos.iterator();
		while (iterador.hasNext()) {
			Aluno proximo = iterador.next();
			System.out.println(proximo);
		}

//		javaColecoes.getAlunos().forEach(a -> {
//			System.out.println(a);
//		});

		System.out.println("O aluno " + a1 + " está matriculado?");
		System.out.println(javaColecoes.estaMatriculado(a1));

		Aluno victor = new Aluno("Victor Antonio", 161094333);
		System.out.println("E esse Victor, está matriculado?");
		System.out.println(javaColecoes.estaMatriculado(victor));

		System.out.println("O 'a1' é equals ao Victor?");
		System.out.println(a1.equals(victor));

		// obrigatoriamente o seguinte é true:

		System.out.println(a1.hashCode() == victor.hashCode());
	}
}
