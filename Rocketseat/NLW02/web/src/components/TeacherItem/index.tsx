import React from 'react';

import whatsappIcon from '../../assets/images/icons/whatsapp.svg';

import './styles.css';

function TeacherItem() {
  return (
    <article className="teacher-item">
      <header>
        <img
          src="https://avatars3.githubusercontent.com/u/32140289?s=460&u=aed5f3cf23d84f0a0d948d9ab5dec4fe8bc6f4b9&v=4"
          alt="Victor Antonio"
        />
        <div>
          <strong>Victor Antonio</strong>
          <span>Programação</span>
        </div>
      </header>

      <p>
        Lorem ipsum dolor, sit amet consectetur adipisicing elit.
        <br /> <br />
        Temporibus assumenda repudiandae doloribus harum autem officia fuga
        fugiat eius? Eius ducimus ipsam doloremque nam quia sequi! Nam, delectus
        veniam.
      </p>

      <footer>
        <p>Preço/hora</p>
        <strong>R$ 100,00</strong>
        <button type="button">
          <img src={whatsappIcon} alt="WhatsApp" />
          Entrar em contato
        </button>
      </footer>
    </article>
  );
}

export default TeacherItem;
