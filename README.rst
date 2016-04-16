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

Python client for Google Cloud Messaging for Android (GCM)

Installation
-------------

.. code-block:: bash

   pip install messengerbot


Usage
------------

Read about `Messenger Platform <https://developers.facebook.com/docs/messenger-platform/send-api-reference>`__

.. code-block:: python

   from messengerbot import MessengerClient, messages, attachments, templates, elements

   messenger = MessengerClient(access_token='your_token')

   # Send text message
   message = messages.Message(text='Hello World')
   request = messages.MessageRequest(self.recipient, message)
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
   request = messages.MessageRequest(self.recipient, message)
   messenger.send(request)


