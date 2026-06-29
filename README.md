### Hexlet tests and linter status:
[![Actions Status](https://github.com/viavinmt-tech/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/viavinmt-tech/python-project-52/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=viavinmt-tech_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=viavinmt-tech_python-project-52)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=viavinmt-tech_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=viavinmt-tech_python-project-52)

# Task Manager

## Description / Описание

**EN:** Task Manager is a web application for creating and tracking tasks. Features include user authentication, task management with statuses and labels, filtering by status, executor, and "my tasks only". Built with Django, Bootstrap 5, PostgreSQL, and deployed on Render.

**RU:** Task Manager — веб-приложение для создания и отслеживания задач. Возможности: регистрация пользователей, управление задачами со статусами и метками, фильтрация по статусу, исполнителю и "только мои задачи". Стек: Django, Bootstrap 5, PostgreSQL, деплой на Render.

## Deployed Application / Деплой

[https://hexlet-code-owdi.onrender.com](https://hexlet-code-owdi.onrender.com)

## Local Development / Локальная разработка

```bash
# Клонирование репозитория
git clone https://github.com/viavinmt-tech/python-project-52.git
cd python-project-52

# Установка зависимостей
make install

# Применение миграций
make migrate

# Запуск сервера
make run

# Запуск тестов с покрытием
make test-coverage
