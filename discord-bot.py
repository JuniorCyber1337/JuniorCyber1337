const prefix = '>'

bot.on('message', (message) => {
       const args = message.content.slice(prefix.length).split(/ +/)
       const command = args.shift().toLowerCase()

        if (command === 'avatar') {
        let user = message.mentions.users.first(); 
        if(!user) user = message.author; // Если нету пинга то берем автора сообщения
        const embed = new Discord.MessageEmbed() // Создаем embed
            .setTitle(user.tag) 
            .setDescription(`[Ссылочка](${user.displayAvatarURL({ size: 2048, dynamic: true })})`) // Гипертекст (Подробнее: https://bit.ly/3g2RVGt)
            .setImage(user.displayAvatarURL({ size: 2048, dynamic: true })) // Аватарка
            .setColor(0x00AE86);
        message.channel.send(embed); // Отправляем embed
  };
});
