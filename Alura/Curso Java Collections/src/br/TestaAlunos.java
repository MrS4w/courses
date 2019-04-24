package br;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;

public class TestaAlunos {
	public static void main(String[] args) {
		Collection<String> alunos = new HashSet<>();
		alunos.add("Victor");
		alunos.add("Antonio");
		alunos.add("Barbosa");
		alunos.add("Silva");

		boolean victorEstaMatriculado = alunos.contains("Victor");
		alunos.remove("Silva");

		System.out.println(victorEstaMatriculado);

		System.out.println(alunos.size());

		for (String aluno : alunos) {
			System.out.println(aluno);
		}

		alunos.forEach(aluno -> {
			System.out.println(aluno);
		});

		System.out.println(alunos);
		
		List<String> alunosEmLista = new ArrayList<>(alunos);
	}
}
