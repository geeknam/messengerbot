messengerbot
======================

.. image:: https://img.shields.io/pypi/v/messengerbot.svg
   :target: https://pypi.python.org/pypi/messengerbot
.. image:: https://img.shields.io/pypi/dm/messengerbot.svg
   :target: https://pypi.python.org/pypi/messengerbot
.. image:: https://secure.travis-ci.org/geeknam/messengerbot.png?branch=master
   :alt: Build Status
   :target: http://travis-ci.org/geeknam/messengerbot
.. image:: https://img.shields.io/gratipay/geeknam.svg
   :target: https://gratipay.com/geeknam/

Python client for Messenger Platform API

Installation
-------------

.. code-block:: bash

   pip install messengerbot


Usage
------------

Read about `Messenger Platform <https://developers.facebook.com/docs/messenger-platform/send-api-reference>`__

.. code-block:: python

   from messengerbot import MessengerClient, messages, attachments, templates, elements

   # Manully initialise client
   messenger = MessengerClient(access_token='your_token')

   # With env var export MESSENGER_PLATFORM_ACCESS_TOKEN=your_token
   from messengerbot import messenger

   recipient = messages.Recipient(recipient_id='123')

   # Send text message
   message = messages.Message(text='Hello World')
   request = messages.MessageRequest(recipient, message)
   messenger.send(request)

   # Send button template
   web_button = elements.WebUrlButton(
      title='Show website',
      url='https://petersapparel.parseapp.com'
   )
   postback_button = elements.PostbackButton(
      title='Start chatting',
      payload='USER_DEFINED_PAYLOAD'
   )
   template = templates.ButtonTemplate(
      text='What do you want to do next?',
      buttons=[
          web_button, postback_button
      ]
   )
   attachment = attachments.TemplateAttachment(template=template)

   message = messages.Message(attachment=attachment)
   request = messages.MessageRequest(recipient, message)
   messenger.send(request)


