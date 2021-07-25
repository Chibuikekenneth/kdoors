/* This example requires Tailwind CSS v2.0+ */
import { Fragment, useState, setState } from 'react'
import { useAxiosGet } from '../Hooks/HttpRequests'
import Loader from '../Components/Loader'
import Select from 'react-select'
import axios from 'axios'

function classNames(...classes) {
  return classes.filter(Boolean).join(' ')
}

export default function User(props) {

  const userUrl = `http://localhost:5000/api/v1/users/`
  const permUrl = `http://localhost:5000/api/v1/permissions/create`

  let users = useAxiosGet(userUrl)

  let usersContent = null

  if (users.error) {
    usersContent = <div>
      <div className="bg-red-300 p-3">
        {users.data}
      </div>
    </div>
  }

  if (users.loading) {
    usersContent = <Loader></Loader>
  }

  const handleOnChange = (userId) => {
    const data = { door_id: props.doorid, user_id: userId }
    axios.post(permUrl, data)
      .then(function (response) {
        props.onUserGet()
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  if (users.data) {

    usersContent =
      <Select options={users.data.map((user) => ({ value: user.id, label: `${user.first_name} ${user.last_name}` }))} onChange={(e) => handleOnChange(e.value)} />
  }

  return (
    <div>
      {usersContent}
    </div>
  )
}
